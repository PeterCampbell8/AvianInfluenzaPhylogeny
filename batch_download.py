#!/usr/bin/env python3
"""
Based on code from
  https://www.biostars.org/p/66921/#188448 by Eli Korvigo
"""
import sys
from Bio import Entrez
import os
import time

#entrez_email = os.environ.get("pete.campbell8@gmail.com")
entrez_email = "pete.campbell8@gmail.com"
if entrez_email:
    Entrez.email = entrez_email

api_key = "e45abf4c745f01fa45b1c6ac9e3b25651208"

RETMAX = 200


def batch_query(accessions_batch, db="nucleotide", retmax=RETMAX, batchsize=199):
    # get GI for query accessions
    query = " ".join(accessions_batch)
    gi_list = []
    try:
        query_handle = Entrez.esearch(
            db=db, term=query, retmax=retmax, field="Accession"
        )
        qh_dict = Entrez.read(query_handle)
        gi_list = qh_dict["IdList"]
        query_handle.close()
    except:
        sys.stderr.write(f"query_handle={query_handle}\n")
    if not gi_list:
        sys.stderr.write(str(qh_dict))
        sys.stderr.write("\n")
        raise RuntimeError("No gi_list returned")

    # get GB files
    search_handle = Entrez.epost(db=db, id=",".join(gi_list))
    try:
        search_results = Entrez.read(search_handle)
    except:
        sys.stderr.write(
            f"query={query}\ngi_list={gi_list}\n\nsearch_handle={search_handle}\n"
        )
        raise
    webenv, query_key = search_results["WebEnv"], search_results["QueryKey"]
    records_handle = Entrez.efetch(
        db=db, rettype="gb", retmax=batchsize, webenv=webenv, query_key=query_key, api_key=api_key, max_tries=6, sleep_between_tries=20
    )

    return records_handle


def batch(accessions, size=199):
    l = len(accessions)
    for start in range(0, l, size):
        yield accessions[start : min(start + size, l)]


def main(acc_fp):
    batchsize = 199
    err = sys.stderr
    verbose = True

    acc_list = []
    with open(acc_fp, "r") as inp:
        tmp = [i.strip() for i in inp]
        acc_list = [i for i in tmp if i]  # skip empty lines
    if not acc_list:
        raise RuntimeError("No accessions found")
    rec_ind = 1
    first = True
    for abatch in batch(acc_list, size=batchsize):
        ofn = f"records-{rec_ind}.gb"
        if os.path.exists(ofn):
            err.write(f"Skipping redownload of {ofn} ...\n")
            rec_ind += len(abatch)
            continue
        if not first:
            err.write(f"Sleeping...\n")
            time.sleep(10)
        first = False
        if verbose:
            err.write(f"Fetching records {rec_ind} to {len(abatch) + rec_ind}\n")
        rec_ind += len(abatch)
        records = batch_query(abatch, batchsize=batchsize)
        tfn = f".tmp-{ofn}"
        try:
            with open(tfn, "w") as out: #multiple TextIOWrapper items but sometimes only 1 getting converted to a string
                for line in records:
                    out.write(line)
            records.close()
        except:
            os.remove(tfn)
            raise Exception("Exception raised")
        else:
            os.rename(tfn, ofn)


if __name__ == "__main__":
    try:
        acc_fp = sys.argv[1]
    except:
        sys.exit("Expected 1 argument: a filepath to a list of accession numbers\n")
    main(acc_fp)

- FASTARandomSampler - Create X number of subgroups with Y number of sequences in each
- treesums - Given the IQTREE reports for the randomly sampled subsets, here are their chosen evolution models
- GB_to_FASTA - Loop through all genbank files and create a simple 2 line fasta combo 1. Record name 2. sequence
- annotation_analysis - Attempt to pull the various components of a genbank annotation. Commented out sections address different sections
- batch_download - Based on code from: https://www.biostars.org/p/66921/#188448 by Eli Korvigo . Takes an accession list and batch downloads GenBank files. Sometimes pulls a file with only a single record and skips over the successive elements.
- missingAccessions - Brute force solution to batch_download's problem. Returns a new accession list describing what was missed on the first pass of batch_download, which can be fed back in until all records are returned.
- feature_analysis - Useful for pulling explicitly defined attributes from GenBank files. In this case, the protein code (e.g., HA)
- removeAmbigAlignments - Given a fasta of sequences, and a specifically formatted file from IQTREE, removes all sequences with a defined % of gaps
- fastaStats - Visualize stats on sequence gaps using a specifically formatted IQTREE summary file
- trimShort - Remove all records in a given protein folder whose sequence is shorter than a given length (for removing bad sequences pre-alignment)

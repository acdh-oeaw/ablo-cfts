# ABLO Central Fulltext Search

Repo to download XML/TEIS from https://api-brucknerlex.acdh.oeaw.ac.at/article and to populate a Typesense based full text search index


## install & run

* create a virtuale env `virtualenv env && source env/bin/activate`
* install needed packages `pip install -U pip && pip install -r requirments.txt`
* run `python dl_xmls` to download XML/TEIs files
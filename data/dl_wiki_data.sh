#!/bin/bash
brew install aria2
aria2c https://s3-us-west-2.amazonaws.com/pinafore-us-west-2/qanta-jmlr-datasets/wikipedia/wiki_lookup.json -x 16 -s 16

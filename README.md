# fasta-native-cpp

C++ fasta benchmark ported from [the benchmark
game](http://benchmarksgame.alioth.debian.org/u64q/program.php?test=fasta&lang=gpp&id=5)
as a node.js addon.

## Install
`npm install kenOfYugen/fasta-native-cpp`

Tested on Arch Linux.

If it doesn't compile on your system, make sure that the dependencies specified in `binding.gyp` are met, and try again.

## Use

```javascript
var fastaCPP = require('fasta-native-cpp');

fastaCPP.run(10);
```

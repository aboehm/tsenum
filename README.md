# tsenum

[![Build Status](https://travis-ci.org/aboehm/tsenum.svg?branch=master)](https://travis-ci.org/aboehm/tsenum)

A timestamp generator.

## Install

You can use pip to install from the repository

```
pip install tsenum
```

or download sources and run pip from this directory

```
git clone https://github.com/aboehm/tsenum
pip install .
```

## Usage (CLI)

Parameter description:

```
usage: tsenum [-h] [-u] -o OFFSET -c COUNT -s {week,day,hour,minute,second} -p
              PATTERN

Timestamp enumerator Count timestamps with different step sizes. A reference
time is used to add/ subtract an offset to enumerate the timestamps. To format
the timestamp strftime formating style is used.

optional arguments:
  -h, --help            show this help message and exit
  -u, --utc             Current time is in UTC
  -o OFFSET, --offset OFFSET
                        Offset to enumerate from
  -c COUNT, --count COUNT
                        Count to enumerate
  -s {week,day,hour,minute,second}, --step {week,day,hour,minute,second}
                        Step width
  -p PATTERN, --pattern PATTERN
                        Date pattern to use (see Python's strftime in
                        datetime)
```

Count 7 days back from yesterday.

```
tsenum --offset -1 --count -7 --step day --pattern "%Y-%m-%d: Hello world!"
2016-05-27: Hello world!
2016-05-28: Hello world!
2016-05-29: Hello world!
2016-05-30: Hello world!
2016-05-31: Hello world!
2016-06-01: Hello world!
2016-06-02: Hello world!
```

Count 3 weeks into future starting from now:

```
tsenum --offset 0 --count 3 --step day --pattern "Week %V"
Week 22
Week 22
Week 23
```

## Usage as module

Count 7 days back from yesterday.

```python
import tsenum
from datetime import datetime

tsenum.enumerate_times(datetime.now(), -1, -7, tsenum.STEP_DAY, '%Y-%m-%d')
```


# mach-eight
Test for Mach Eight job

## Prerequisites
- Python 3

## Execution
```
python3 app.py <list of numbers comma-separated> <expected sum>
```

for example
```
python3 app.py 1,9,5,0,20,-4,12,16,7 12
```

## Unit test execution
```
python3 -m unittest test.py
```

If you want to include more unit test create the files inside the folder /test_cases with the following structure
```
<list of numbers comma-separated>
<expected sum>
<pair result 1 comma-separated>
<pair result 2 comma-separated>
...
<pair result n comma-separated>
```

For example
```
0,1,2,3,4,5
5
0,5
1,4
2,3
```

# Loop

`xrange()` generates and lazily evaluate a sequence (list) of numbers defined by the range defined in the parameter. It returns a `xrange` object that you can use for iterating a collection. Whereas `range()` creates the sequence of numbers in memory. Pick `xrange()` or `range()` to suit your needs. However, Python3 only supports `range()` - no `xrange()` - as Python3 merges the efficiency of `xrange()`  into `range()`.

## Loop Constructs in Other Languages

|            | Range Style               | Closure Style | For-Loop Style                      |
|------------|---------------------------|---------------|-------------------------------------|
| Javascript |                           | `forEach`     | `for (let x of array) { }`          |
| Python     | `range(n)` or `xrange(n)` |               | `for x in array:`                   |
| Swift      | `0..<n`                   | `forEach`     | `for x in array { }`                |
| Java       |                           |               | `for (T x: array) { }`              |
| Bash       | `{0..n}`                  | `forEach`     | `for x in ${array[@]}; do ... done` |
| Go         | `                         |               | `for i, x in range array { }`       |



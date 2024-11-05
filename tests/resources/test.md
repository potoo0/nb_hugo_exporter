+++
date = 2024-11-05
title = "Test"
draft = false
+++

### md cell

- row1
- row2
RAW cell

{{< jp_codecell_input ecnt=1 >}}
```python
"direct"
```
{{< /jp_codecell_input >}}

{{< jp_codecell_output ecnt=1 dst="stdout" >}}



'direct'

{{< /jp_codecell_output >}}


{{< jp_codecell_input ecnt=2 >}}
```python
print("stdout")
```
{{< /jp_codecell_input >}}

{{< jp_codecell_output ecnt=2 dst="stdout" >}}
stdout
{{< /jp_codecell_output >}}


{{< jp_codecell_input ecnt=3 >}}
```python
import sys
print("stderr", file=sys.stderr)
```
{{< /jp_codecell_input >}}

{{< jp_codecell_output ecnt=3 dst="stderr" >}}
stderr
{{< /jp_codecell_output >}}


{{< jp_codecell_input ecnt=4 >}}
```python
from IPython.display import JSON

JSON({1: 2, 3: 4})
```
{{< /jp_codecell_input >}}

{{< jp_codecell_output ecnt=4 dst="stdout" >}}
{"1": 2, "3": 4}
{{< /jp_codecell_output >}}


{{< jp_codecell_input ecnt=5 >}}
```python
import time
time.sleep(10)

```
{{< /jp_codecell_input >}}

{{< jp_codecell_output ecnt=5 dst="stderr" >}}
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[5], line 2
      1 import time
----> 2 time.sleep(10)

KeyboardInterrupt: 
{{< /jp_codecell_output >}}


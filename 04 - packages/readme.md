## import packages

#### folder structure
```bash
mypackages
|
+---- __init__.py
+---- demopack.py
+---- subpack
      |
      +---- __init__.py
      +---- subdemopack.py
```

```python
import mypackages.demopack
import mypackages.demopack as dp
>>> mypackages.demopack.packprint()
>>> dp.packprint()


from mypackages import demopack as dp
>>> dp.packprint()
>>> dp.packprint1()


from mypackages.demopack import packprint as pp
from mypackages.demopack import packprint1 as pp1
>>> pp()
>>> pp1()

## subpackages
from mypackages.subpack import subdemopack as sdp
>>> sdp.subpackprint()
>>> sdp.subpackprint1()

from mypackages.subpack.subdemopack import subpackprint as spp
>>> spp()
```

#### python codes
```python
# demopack.py
def packprint():
    print("This is demo packages")

def packprint1():
    print("This is demo packages 1")
```
```python
# subdemopack.py
def subpackprint():
    print("This is sub demo packages")

def subpackprint1():
    print("This is sub demo packages 1")
```

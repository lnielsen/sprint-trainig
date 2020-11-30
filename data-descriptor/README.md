# Data descriptors

Examples of data descriptors:

```python
@property
@classmethod
@staticmethod
```

ORM/Schema example:

```python
class MyModel(db.Model):
    id = db.Column(db.Integer)


class MySchema(Schema):
    id = fields.Integer()
```

How does a data descriptor look like?

```python
class MyDescriptor:
    def __get__(self, obj, objtype=None):
        # ...

    def __set__(self, obj, value):
        # ...

    def __set_name__(self, obj, value):
        # ...
```


Exercise time! Go to ``exercise.py`` and implement the ``SystemField``.


### Bonus - Method Resolution Order (MRO)

```python
class A:
    def __init__(self):
        print("I am a A")
        super().__init__()

class B(A):
    def __init__(self):
        print("I am a B")
        super().__init__()

class C(A):
    def __init__(self):
        print("I am a C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("I am a D")
        super().__init__()

d1 = D()
```

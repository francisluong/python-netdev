#!/usr/bin/env python

def class_with_method(func):
	class klass: pass
	setattr(klass, func.__name__, func)
	return klass

def say_foo(self):
	print "foo"

Foo = class_with_method(say_foo)
foo = Foo()
foo.say_foo()

from new import classobj

Foo2 = classobj("Foo2",(Foo,),{'bar':lambda self:'bar'})
foo2 = Foo2()
#Foo2.bar() #TypeError: unbound method <lambda>() must be called with Foo2 instance as first argument (got nothing instead)
foo2.say_foo()

##############
print "---"

def howdy(self, you):
	print ("Howdy, " + you)

# name, baseclass_tuple, fields_methods_dict
MyList = type("MyList",(list,), dict(x=42, howdy=howdy))

ml = MyList()
ml.append("Camembert")
print ml
print(ml.x)
ml.howdy("Jon")
print ml.__class__
print ml.__class__.__class__

###################

print("\n== Hooking the Meta ==")
class SimpleMeta1(type):
	def __init__(cls, name, bases, nmspc):
		super(SimpleMeta1, cls).__init__(name, bases, nmspc)
		cls.uses_metaclass = lambda self: "Yes!"

class Simple1(object):
	__metaclass__ = SimpleMeta1
	def foo(self): pass

	@staticmethod
	def bar(): pass

simple = Simple1
print( [m for m in dir(simple) if not m.startswith('__')] )


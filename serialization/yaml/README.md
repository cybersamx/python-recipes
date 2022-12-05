# YAML Serialization

There are several ways to perform yaml serialization and deserialization using the [PyYaml](https://pyyaml.org) package.

* [YAML-dictionary serialization](dict) - Serialization/deserialization of non-nested yaml to/from python dictionary.
* [YAML-object serialization using the SafeLoader](safe-loader) - Serialization/deserialization of nested yaml to/from python custom object using PyYaml's `SafeLoader` class, `YAMLObject` class and `add_constructor` class method. 
* [YAML-object serialization using the UnsafeLoader](unsafe-loader) - Serialization/deserialization of nested yaml to/from python custom object using PyYaml's `UnsafeLoader` class.

---
layout: default
title: pymatgen.alchemy.transmuters.md
nav_exclude: true
---

# pymatgen.alchemy.transmuters module

This module implements various transmuter classes.
Transmuters are essentially classes that generate TransformedStructures from
various data sources. They enable the high-throughput generation of new
structures and input files.

It also includes the helper function, batch_write_vasp_input to generate an
entire directory of vasp input files for running.


### _class_ pymatgen.alchemy.transmuters.CifTransmuter(cif_string, transformations=None, primitive=True, extend_collection=False)
Bases: `StandardTransmuter`

Generates a Transmuter from a cif string, possibly containing multiple
structures.

Generates a Transmuter from a cif string, possibly
containing multiple structures.


* **Parameters**


    * **cif_string** – A string containing a cif or a series of cifs


    * **transformations** – New transformations to be applied to all
    structures


    * **primitive** – Whether to generate the primitive cell from the cif.


    * **extend_collection** – Whether to use more than one output structure
    from one-to-many transformations. extend_collection can be a
    number, which determines the maximum branching for each
    transformation.



#### _static_ from_filenames(filenames, transformations=None, primitive=True, extend_collection=False)
Generates a TransformedStructureCollection from a cif, possibly
containing multiple structures.


* **Parameters**


    * **filenames** – List of strings of the cif files


    * **transformations** – New transformations to be applied to all
    structures


    * **primitive** – Same meaning as in __init__.


    * **extend_collection** – Same meaning as in __init__.



### _class_ pymatgen.alchemy.transmuters.PoscarTransmuter(poscar_string, transformations=None, extend_collection=False)
Bases: `StandardTransmuter`

Generates a transmuter from a sequence of POSCARs.


* **Parameters**


    * **poscar_string** – List of POSCAR strings


    * **transformations** – New transformations to be applied to all
    structures.


    * **extend_collection** – Whether to use more than one output structure
    from one-to-many transformations.



#### _static_ from_filenames(poscar_filenames, transformations=None, extend_collection=False)
Convenient constructor to generates a POSCAR transmuter from a list of
POSCAR filenames.


* **Parameters**


    * **poscar_filenames** – List of POSCAR filenames


    * **transformations** – New transformations to be applied to all
    structures.


    * **extend_collection** – Same meaning as in __init__.



### _class_ pymatgen.alchemy.transmuters.StandardTransmuter(transformed_structures, transformations=None, extend_collection=0, ncores=None)
Bases: `object`

An example of a Transmuter object, which performs a sequence of
transformations on many structures to generate TransformedStructures.

<!-- attribute: transformed_structures

List of all transformed structures. -->
Initializes a transmuter from an initial list of
[`pymatgen.alchemy.materials.TransformedStructure`](pymatgen.alchemy.materials.md#pymatgen.alchemy.materials.TransformedStructure).


* **Parameters**


    * **transformed_structures** (*[*[*TransformedStructure*](pymatgen.alchemy.materials.md#pymatgen.alchemy.materials.TransformedStructure)*]*) – Input transformed
    structures


    * **transformations** (*[**Transformations**]*) – New transformations to be
    applied to all structures.


    * **extend_collection** (*int*) – Whether to use more than one output
    structure from one-to-many transformations. extend_collection
    can be an int, which determines the maximum branching for each
    transformation.


    * **ncores** (*int*) – Number of cores to use for applying transformations.
    Uses multiprocessing.Pool. Default is None, which implies
    serial.



#### add_tags(tags)
Add tags for the structures generated by the transmuter.


* **Parameters**

    **tags** – A sequence of tags. Note that this should be a sequence of
    strings, e.g., [“My awesome structures”, “Project X”].



#### append_transformation(transformation, extend_collection=False, clear_redo=True)
Appends a transformation to all TransformedStructures.


* **Parameters**


    * **transformation** – Transformation to append


    * **extend_collection** – Whether to use more than one output structure
    from one-to-many transformations. extend_collection can be a
    number, which determines the maximum branching for each
    transformation.


    * **clear_redo** (*bool*) – Whether to clear the redo list. By default,
    this is True, meaning any appends clears the history of
    undoing. However, when using append_transformation to do a
    redo, the redo list should not be cleared to allow multiple
    redos.



* **Returns**

    List of booleans corresponding to initial transformed structures
    each boolean describes whether the transformation altered the
    structure



#### append_transformed_structures(tstructs_or_transmuter)
Method is overloaded to accept either a list of transformed structures
or transmuter, it which case it appends the second transmuter”s
structures.


* **Parameters**

    **tstructs_or_transmuter** – A list of transformed structures or a
    transmuter.



#### apply_filter(structure_filter)
Applies a structure_filter to the list of TransformedStructures
in the transmuter.


* **Parameters**

    **structure_filter** – StructureFilter to apply.



#### extend_transformations(transformations)
Extends a sequence of transformations to the TransformedStructure.


* **Parameters**

    **transformations** – Sequence of Transformations



#### _static_ from_structures(structures, transformations=None, extend_collection=0)
Alternative constructor from structures rather than
TransformedStructures.


* **Parameters**


    * **structures** – Sequence of structures


    * **transformations** – New transformations to be applied to all
    structures


    * **extend_collection** – Whether to use more than one output structure
    from one-to-many transformations. extend_collection can be a
    number, which determines the maximum branching for each
    transformation.



* **Returns**

    StandardTransmuter



#### redo_next_change()
Redo the last undone transformation in the TransformedStructure.


* **Raises**

    **IndexError if already at the latest change.** –



#### set_parameter(key, value)
Add parameters to the transmuter. Additional parameters are stored in
the as_dict() output.


* **Parameters**


    * **key** – The key for the parameter.


    * **value** – The value for the parameter.



#### undo_last_change()
Undo the last transformation in the TransformedStructure.


* **Raises**

    **IndexError if already at the oldest change.** –



#### write_vasp_input(\*\*kwargs)
Batch write vasp input for a sequence of transformed structures to
output_dir, following the format output_dir/{formula}_{number}.


* **Parameters**

    **kwargs** – All kwargs supported by batch_write_vasp_input.



### pymatgen.alchemy.transmuters.batch_write_vasp_input(transformed_structures: Sequence[TransformedStructure], vasp_input_set: type[VaspInputSet] = <class 'pymatgen.io.vasp.sets.MPRelaxSet'>, output_dir: str = '.', create_directory: bool = True, subfolder: Callable[[TransformedStructure], str] | None = None, include_cif: bool = False, \*\*kwargs)
Batch write vasp input for a sequence of transformed structures to
output_dir, following the format output_dir/{group}/{formula}_{number}.


* **Parameters**


    * **transformed_structures** – Sequence of TransformedStructures.


    * **vasp_input_set** – pymatgen.io.vasp.sets.VaspInputSet to creates
    vasp input files from structures.


    * **output_dir** – Directory to output files


    * **create_directory** (*bool*) – Create the directory if not present.
    Defaults to True.


    * **subfolder** – Function to create subdirectory name from
    transformed_structure.
    e.g., lambda x: x.other_parameters[“tags”][0] to use the first
    tag.


    * **include_cif** (*bool*) – Boolean indication whether to output a CIF as
    well. CIF files are generally better supported in visualization
    programs.


    * **\*\*kwargs** – Any kwargs supported by vasp_input_set.
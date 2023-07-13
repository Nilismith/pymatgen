"""Write Prismatic (http://prism-em.com) input files."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pymatgen.core import Structure


class Prismatic:
    """
    Class to write Prismatic  (http://prism-em.com/) input files.
    This is designed for STEM image simulation.
    """

    def __init__(self, structure: Structure, comment: str = "Generated by pymatgen") -> None:
        """
        Args:
            structure: pymatgen Structure
            comment (str): comment.
        """
        self.structure = structure
        self.comment = comment

    def to_string(self) -> str:
        """
        Returns: Prismatic XYZ file. This is similar to XYZ format
        but has specific requirements for extra fields, headers, etc.
        """
        lattice = self.structure.lattice
        lines = [self.comment, " ".join(map(str, lattice.lengths))]
        for site in self.structure:
            for sp, occu in site.species.items():
                x, y, z = site.coords
                lines.append(f"{sp.Z} {x} {y} {z} {occu} {site.properties.get('thermal_sigma', 0)}")

        lines.append("-1")

        return "\n".join(lines)

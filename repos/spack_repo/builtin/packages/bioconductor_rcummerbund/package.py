# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.r import RPackage

from spack.package import *


class BioconductorRcummerbund(RPackage):
    """Allows for persistent storage, access, exploration, and manipulation of
    Cufflinks high-throughput sequencing data. In addition, provides numerous
    plotting functions for commonly used visualizations."""

    homepage = "https://www.bioconductor.org/packages/release/bioc/html/cummeRbund.html"
    url = "https://bioconductor.posit.co/packages/3.21/bioc/src/contrib/cummeRbund_2.48.0.tar.gz"

    bioc = "cummeRbund"

    maintainers("meyersbs")

    license("Artistic-2.0", checked_by="meyersbs")

    version(
        "2.50.0",
        sha256="887ad38f0fa6cf7910d49ac812b46b4742e2495bf28dfe16e891dc1f5d663fc4",
    )
    version(
        "2.48.0",
        sha256="1380ce31f9189b443b892a09cbe0e7119582647c8eb9a4f1c7ef33fe692ea08c",
    )

    depends_on("r@2.7.0:", type=("build", "run"))
    depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-fastcluster", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))

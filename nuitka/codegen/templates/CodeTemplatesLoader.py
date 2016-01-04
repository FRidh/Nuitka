#     Copyright 2016, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Templates for the loading of embedded modules.

"""


template_metapath_loader_compiled_module_entry = """\
{ (char *)"%(module_name)s", MOD_INIT_NAME( %(module_identifier)s ), NUITKA_COMPILED_MODULE },"""

template_metapath_loader_compiled_package_entry = """\
{ (char *)"%(module_name)s", MOD_INIT_NAME( %(module_identifier)s ), NUITKA_COMPILED_PACKAGE },"""

template_metapath_loader_shlib_module_entry = """\
{ (char *)"%(module_name)s", NULL, NUITKA_SHLIB_MODULE },"""

template_metapath_loader_body = """\
// Code tegister embedded modules if any.
#if %(use_loader)d == 1

#include "nuitka/unfreezing.hpp"

// Table for lookup to find "frozen" modules or DLLs, i.e. the ones included in
// or along this binary.
%(metapath_module_decls)s
static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] =
{
%(metapath_loader_inittab)s
    { NULL, NULL, 0 }
};

void setupMetaPathBasedLoader( void )
{
    static bool init_done = false;

    if ( init_done == false )
    {
        registerMetaPathBasedUnfreezer( meta_path_loader_entries );
        init_done = true;
    }
}
#else

void setupMetaPathBasedLoader( void )
{
}

#endif
"""

from . import TemplateDebugWrapper # isort:skip
TemplateDebugWrapper.checkDebug(globals())

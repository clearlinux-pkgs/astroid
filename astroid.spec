#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astroid
Version  : 1.6.3
Release  : 56
URL      : https://pypi.python.org/packages/c7/fc/7a6e48b7bea11e53cab81fcb463c943167c274cafa98bf8faca69129b3bb/astroid-1.6.3.tar.gz
Source0  : https://pypi.python.org/packages/c7/fc/7a6e48b7bea11e53cab81fcb463c943167c274cafa98bf8faca69129b3bb/astroid-1.6.3.tar.gz
Summary  : A abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: astroid-python3
Requires: astroid-license
Requires: astroid-python
Requires: backports.functools_lru_cache
Requires: enum34
Requires: lazy-object-proxy
Requires: six
Requires: wrapt
BuildRequires : lazy-object-proxy
BuildRequires : logilab-common
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
=======

%package license
Summary: license components for the astroid package.
Group: Default

%description license
license components for the astroid package.


%package python
Summary: python components for the astroid package.
Group: Default
Requires: astroid-python3

%description python
python components for the astroid package.


%package python3
Summary: python3 components for the astroid package.
Group: Default
Requires: python3-core

%description python3
python3 components for the astroid package.


%prep
%setup -q -n astroid-1.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529091073
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/astroid
cp COPYING.LESSER %{buildroot}/usr/share/doc/astroid/COPYING.LESSER
cp COPYING %{buildroot}/usr/share/doc/astroid/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/astroid/COPYING
/usr/share/doc/astroid/COPYING.LESSER

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

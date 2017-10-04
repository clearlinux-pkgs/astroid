#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astroid
Version  : 1.5.3
Release  : 37
URL      : https://pypi.debian.net/astroid/astroid-1.5.3.tar.gz
Source0  : https://pypi.debian.net/astroid/astroid-1.5.3.tar.gz
Summary  : A abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: astroid-legacypython
Requires: astroid-python3
Requires: astroid-python
Requires: enum34
Requires: lazy-object-proxy
Requires: six
Requires: wrapt
BuildRequires : enum34
BuildRequires : lazy-object-proxy
BuildRequires : logilab-common
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
=======

%package legacypython
Summary: legacypython components for the astroid package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the astroid package.


%package python
Summary: python components for the astroid package.
Group: Default
Requires: astroid-legacypython
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
%setup -q -n astroid-1.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507148705
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :
%install
export SOURCE_DATE_EPOCH=1507148705
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

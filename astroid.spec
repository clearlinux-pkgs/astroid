#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astroid
Version  : 2.2.2
Release  : 74
URL      : https://files.pythonhosted.org/packages/de/4e/cd4220cee9f2aa3e58708abf57e4820e0d9632ab1193b8e3097bf6503a4b/astroid-2.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/de/4e/cd4220cee9f2aa3e58708abf57e4820e0d9632ab1193b8e3097bf6503a4b/astroid-2.2.2.tar.gz
Summary  : a graphical threads-with-tags style, lightweight and fast, email client for notmuch, inspired by sup and others
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: astroid-license = %{version}-%{release}
Requires: astroid-python = %{version}-%{release}
Requires: astroid-python3 = %{version}-%{release}
Requires: enum34
Requires: lazy-object-proxy
Requires: six
Requires: typed-ast
Requires: typing
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : lazy-object-proxy
BuildRequires : logilab-common
BuildRequires : pytest-runner
BuildRequires : six

%description
Astroid
=======
.. image:: https://travis-ci.org/PyCQA/astroid.svg?branch=master
:target: https://travis-ci.org/PyCQA/astroid

%package license
Summary: license components for the astroid package.
Group: Default

%description license
license components for the astroid package.


%package python
Summary: python components for the astroid package.
Group: Default
Requires: astroid-python3 = %{version}-%{release}

%description python
python components for the astroid package.


%package python3
Summary: python3 components for the astroid package.
Group: Default
Requires: python3-core

%description python3
python3 components for the astroid package.


%prep
%setup -q -n astroid-2.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551582833
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/astroid
cp COPYING %{buildroot}/usr/share/package-licenses/astroid/COPYING
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/astroid/COPYING.LESSER
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/astroid/COPYING
/usr/share/package-licenses/astroid/COPYING.LESSER

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

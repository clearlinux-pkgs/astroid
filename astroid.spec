#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astroid
Version  : 1.3.8
Release  : 17
URL      : https://pypi.python.org/packages/source/a/astroid/astroid-1.3.8.tar.gz
Source0  : https://pypi.python.org/packages/source/a/astroid/astroid-1.3.8.tar.gz
Summary  : A abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: astroid-python
BuildRequires : logilab-common
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
.. image:: https://drone.io/bitbucket.org/logilab/astroid/status.png
:alt: drone.io Build Status
:target: https://drone.io/bitbucket.org/logilab/astroid

%package python
Summary: python components for the astroid package.
Group: Default

%description python
python components for the astroid package.


%prep
%setup -q -n astroid-1.3.8

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

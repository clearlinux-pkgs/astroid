#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : astroid
Version  : 2.3.2
Release  : 85
URL      : https://files.pythonhosted.org/packages/94/32/58db7000d735f1f6e4b60c8ae0137b96b227e3ec4b640d8cf28f16e5bf62/astroid-2.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/94/32/58db7000d735f1f6e4b60c8ae0137b96b227e3ec4b640d8cf28f16e5bf62/astroid-2.3.2.tar.gz
Summary  : An abstract syntax tree for Python with inference support.
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: astroid-license = %{version}-%{release}
Requires: astroid-python = %{version}-%{release}
Requires: astroid-python3 = %{version}-%{release}
Requires: lazy-object-proxy
Requires: six
Requires: typed_ast
Requires: wrapt
BuildRequires : buildreq-distutils3
BuildRequires : lazy-object-proxy
BuildRequires : logilab-common
BuildRequires : pytest
BuildRequires : pytest-runner
BuildRequires : six
BuildRequires : typed_ast
BuildRequires : wrapt
Patch1: 0001-Unfreeze-six-dependency.patch

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
%setup -q -n astroid-2.3.2
cd %{_builddir}/astroid-2.3.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572998594
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m unittest discover -s astroid/tests -p "unittest*.py" || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/astroid
cp %{_builddir}/astroid-2.3.2/COPYING %{buildroot}/usr/share/package-licenses/astroid/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/astroid-2.3.2/COPYING.LESSER %{buildroot}/usr/share/package-licenses/astroid/9a1929f4700d2407c70b507b3b2aaf6226a9543c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/astroid/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/astroid/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

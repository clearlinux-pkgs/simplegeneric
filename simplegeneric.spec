#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simplegeneric
Version  : 0.8.1
Release  : 45
URL      : http://pypi.debian.net/simplegeneric/simplegeneric-0.8.1.zip
Source0  : http://pypi.debian.net/simplegeneric/simplegeneric-0.8.1.zip
Summary  : Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)
Group    : Development/Tools
License  : ZPL-2.1
Requires: simplegeneric-python = %{version}-%{release}
Requires: simplegeneric-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=========================
Trivial Generic Functions
=========================
* New in 0.8: Source and tests are compatible with Python 3 (w/o ``setup.py``)
* 0.8.1: setup.py is now compatible with Python 3 as well
* New in 0.7: `Multiple Types or Objects`_
* New in 0.6: `Inspection and Extension`_, and thread-safe method registration

%package python
Summary: python components for the simplegeneric package.
Group: Default
Requires: simplegeneric-python3 = %{version}-%{release}

%description python
python components for the simplegeneric package.


%package python3
Summary: python3 components for the simplegeneric package.
Group: Default
Requires: python3-core

%description python3
python3 components for the simplegeneric package.


%prep
%setup -q -n simplegeneric-0.8.1
cd %{_builddir}/simplegeneric-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576015743
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
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

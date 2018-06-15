#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simplegeneric
Version  : 0.8.1
Release  : 33
URL      : http://pypi.debian.net/simplegeneric/simplegeneric-0.8.1.zip
Source0  : http://pypi.debian.net/simplegeneric/simplegeneric-0.8.1.zip
Summary  : Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)
Group    : Development/Tools
License  : ZPL-2.1
Requires: simplegeneric-python3
Requires: simplegeneric-python
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: simplegeneric-python3

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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523307719
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

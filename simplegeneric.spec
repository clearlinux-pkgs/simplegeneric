#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : simplegeneric
Version  : 0.8.1
Release  : 21
URL      : https://pypi.python.org/packages/source/s/simplegeneric/simplegeneric-0.8.1.zip
Source0  : https://pypi.python.org/packages/source/s/simplegeneric/simplegeneric-0.8.1.zip
Summary  : Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)
Group    : Development/Tools
License  : ZPL-2.1
Requires: simplegeneric-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
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

%description python
python components for the simplegeneric package.


%prep
%setup -q -n simplegeneric-0.8.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484575347
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1484575347
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

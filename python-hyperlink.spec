Summary:	A featureful, immutable, and correct URL for Python
Name:		python-hyperlink
Version:	21.0.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/hyperlink
Source0:	https://files.pythonhosted.org/packages/3a/51/1947bd81d75af87e3bb9e34593a4cf118115a8feb451ce7a69044ef1412e/hyperlink-21.0.0.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Python library for finite-state machines
Hyperlink is a featureful, pure-Python implementation of the URL,
with an emphasis on correctness. BSD licensed.

%package -n python2-hyperlink
Summary:	A featureful, immutable, and correct URL for Python
Group:		Development/Python

%description -n python2-hyperlink
Python library for finite-state machines


%prep
%setup -qn hyperlink-%{version}
%autopatch -p1

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/hyperlink
%{py_sitedir}/*.egg-info

%files -n python2-hyperlink
%{py2_puresitedir}/hyperlink
%{py2_puresitedir}/*.egg-info

Summary:	A featureful, immutable, and correct URL for Python
Name:		python-hyperlink
Version:	18.0.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/hyperlink
Source0:	https://files.pythonhosted.org/packages/de/05/b8e453085cf8a7f27bb1226596f4ccf5cc9e758377d60284f990bbdc592c/hyperlink-%{version}.tar.gz
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

%prep
%setup -qn hyperlink-%{version}
%apply_patches

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

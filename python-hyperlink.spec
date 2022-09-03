Summary:	A featureful, immutable, and correct URL for Python
Name:		python-hyperlink
Version:	21.0.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/hyperlink
Source0:	https://files.pythonhosted.org/packages/3a/51/1947bd81d75af87e3bb9e34593a4cf118115a8feb451ce7a69044ef1412e/hyperlink-21.0.0.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Python library for finite-state machines
Hyperlink is a featureful, pure-Python implementation of the URL,
with an emphasis on correctness. BSD licensed.

%prep
%setup -qn hyperlink-%{version}
%autopatch -p1

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{py_sitedir}/hyperlink
%{py_sitedir}/*.egg-info

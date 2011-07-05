%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		python-prettytable
Version:	0.5
Release:	1%{?dist}
Summary:	Python library to display tabular data in tables

Group:		Development/Languages
License:	BSD
Source0:	http://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.5.tar.gz
URL:		http://pypi.python.org/pypi/PrettyTable
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:	python-devel

%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%prep
%setup -q -n prettytable-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{python_sitelib}/*


%changelog
* Wed Jun 29 2011 Chris Lalancette <clalance@redhat.com> - 0.5-1
- Initial package.
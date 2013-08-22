%{?scl:%scl_package python-prettytable}
%{!?scl:%global pkg_name %{name}}

%global modname prettytable

Name:           %{?scl_prefix}python-%{modname}
Version:	0.6.1
Release:	2%{?dist}
Summary:	Python library to display tabular data in tables

Group:		Development/Languages
License:	BSD
Source0:    http://pypi.python.org/packages/source/P/PrettyTable/%{modname}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/PrettyTable

BuildArch:	noarch
BuildRequires:  %{?scl_prefix}python2-devel
BuildRequires:  %{?scl_prefix}python-setuptools


%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.


%prep
%setup -q -n %{modname}-%{version}


%build
%{?scl:scl enable %{scl} "}
%{__python} setup.py build
%{?scl:"}


%check
%{?scl:scl enable %{scl} "}
%{__python} %{modname}_test.py
%{?scl:"}


%install
%{?scl:scl enable %{scl} "}
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{?scl:"}


%files
%doc README COPYING CHANGELOG
%{python_sitelib}/%{modname}.py*
%{python_sitelib}/%{modname}-%{version}*


%changelog
* Thu Aug 22 2013 apevec@redhat.com 0.6.1-2
- python27 SCL version

* Tue Aug 07 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- New upstream version
- Added support for python3
- Included README, COPYING, and CHANGELOG in docs

* Tue Aug 07 2012 Pádraig Brady <P@draigBrady.com> - 0.6-1
- Update to 0.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.5-2
- BuildRequire python-setuptools

* Wed Jun 29 2011 Chris Lalancette <clalance@redhat.com> - 0.5-1
- Initial package.

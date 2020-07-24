%global sname pg_stat_kcache

%global kcachemajver 2
%global kcachemidver 1
%global kcacheminver 3

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_compiler_at10
%endif

Summary:	A PostgreSQL extension gathering CPU and disk acess statistics
Name:		%{sname}%{pgmajorversion}
Version:	%{kcachemajver}.%{kcachemidver}.%{kcacheminver}
Release:	1%{?dist}
License:	PostgreSQL
URL:		https://github.com/powa-team/%{sname}
Source0:	https://github.com/powa-team/%{sname}/archive/REL%{kcachemajver}_%{kcachemidver}_%{kcacheminver}.tar.gz
Patch0:		%{sname}-pg%{pgmajorversion}-makefile-pgxs.patch
BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros
Requires:	postgresql%{pgmajorversion}-server

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_min_requires
%endif

%description
Gathers statistics about real reads and writes done by the filesystem layer.
It is provided in the form of an extension for PostgreSQL >= 9.4., and
requires pg_stat_statements extension to be installed. PostgreSQL 9.4 or more
is required as previous version of provided pg_stat_statements didn't expose
the queryid field.

%prep
%setup -q -n %{sname}-REL%{kcachemajver}_%{kcachemidver}_%{kcacheminver}
%patch0 -p0

%build
%ifarch ppc64 ppc64le
	%pgdg_set_ppc64le_compiler_flags
%endif
%{__make} USE_PGXS=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%{__make} USE_PGXS=1 %{?_smp_mflags} install DESTDIR=%{buildroot}

# Install README
%{__install} -d %{buildroot}%{pginstdir}/doc/extension/
%{__install} README.rst %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.rst

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{pginstdir}/doc/extension/README-%{sname}.rst
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}--*.sql
%{pginstdir}/share/extension/%{sname}.control
%if %{pgmajorversion} >= 11 && %{pgmajorversion} < 90
 %if 0%{?rhel} && 0%{?rhel} <= 6
 %else
 %{pginstdir}/lib/bitcode/%{sname}*.bc
 %{pginstdir}/lib/bitcode/%{sname}/*.bc
 %endif
%endif

%changelog
* Thu Jul 9 2020 Devrim Gündüz <devrim@gunduz.org> - 2.1.3-1
- Update to 2.1.3

* Thu Jul 9 2020 Devrim Gündüz <devrim@gunduz.org> - 2.1.2-1
- Update to 2.1.2

* Thu Sep 26 2019 Devrim Gündüz <devrim@gunduz.org>
- Rebuild for PostgreSQL 12

* Mon Oct 15 2018 Devrim Gündüz <devrim@gunduz.org>
- Rebuild against PostgreSQL 11.0

* Wed Aug 1 2018 - Devrim Gündüz <devrim@gunduz.org> 2.1.1-1
- Update 2.1.1

* Thu Jul 26 2018 - Devrim Gündüz <devrim@gunduz.org> 2.1.0-1
- Update 2.1.0

* Sun Apr 15 2018 - Devrim Gündüz <devrim@gunduz.org> 2.0.3-2
- Update to new URL, and use macros for version numberto avoid issues.

* Wed Oct 12 2016 - Devrim Gündüz <devrim@gunduz.org> 2.0.3-1
- Update to 2.0.3

* Fri Mar 27 2015 - Devrim Gündüz <devrim@gunduz.org> 2.0.2-1
- Update to 2.0.2

* Tue Mar 17 2015 - Devrim Gündüz <devrim@gunduz.org> 2.0.1-1
- Initial RPM packaging for PostgreSQL RPM Repository

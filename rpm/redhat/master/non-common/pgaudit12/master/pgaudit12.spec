%global sname	pgaudit

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_compiler_at10
%endif

Summary:	PostgreSQL Audit Extension
Name:		%{sname}12_%{pgmajorversion}
Version:	1.2.2
Release:	1%{?dist}
License:	BSD
Source0:	https://github.com/%{sname}/%{sname}/archive/%{version}.tar.gz
Patch0:		%{sname}-pg%{pgmajorversion}-makefile-pgxs.patch
URL:		https://www.pgaudit.org
BuildRequires:	postgresql%{pgmajorversion}-devel postgresql%{pgmajorversion}
BuildRequires:	pgdg-srpm-macros
Requires:	postgresql%{pgmajorversion}-server

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_min_requires
%endif

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.

%prep
%setup -q -n %{sname}-%{version}
%patch0 -p0

%build
%ifarch ppc64 ppc64le
	%pgdg_set_ppc64le_compiler_flags
%endif
%{__make} USE_PGXS=1 %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make}  USE_PGXS=1 %{?_smp_mflags} DESTDIR=%{buildroot} install
# Install README and howto file under PostgreSQL installation directory:
%{__install} -d %{buildroot}%{pginstdir}/doc/extension
%{__install} -m 644 README.md %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.md
%{__rm} -f %{buildroot}%{pginstdir}/doc/extension/README.md

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{pginstdir}/doc/extension/README-%{sname}.md
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/pgaudit-*.sql
%{pginstdir}/share/extension/%{sname}.control

%changelog
* Tue Oct 6 2020 Devrim Gündüz <devrim@gunduz.org> - 1.2.2-1
- Update to 1.2.2

* Sun May 10 2020 Devrim Gündüz <devrim@gunduz.org> - 1.2.1-2
- Fix pgdg-srpm-macros dependency. Per John.

* Wed Apr 1 2020 - Devrim Gündüz <devrim@gunduz.org> 1.2.1-1
- Update to 1.2.1
- Add missing BR and Requires
- Switch to pgdg-srpm-macros

* Mon Oct 15 2018 Devrim Gündüz <devrim@gunduz.org> - 1.2.0-1.1
- Rebuild against PostgreSQL 11.0

* Wed Jan 24 2018 - Devrim Gündüz <devrim@gunduz.org> 1.2.0-1
- Update to 1.2.0

* Tue Jun 6 2017 - Devrim Gündüz <devrim@gunduz.org> 1.1.0-1
- Update to 1.1.0

* Thu Oct 27 2016 - Devrim Gündüz <devrim@gunduz.org> 1.0.0-1
- Update to 1.0.0

* Fri Oct 21 2016 - Devrim Gündüz <devrim@gunduz.org> 0.0.4-1
- Initial RPM packaging for PostgreSQL RPM Repository

%global sname pg_fkpart

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_compiler_at10
%endif

Summary:	PostgreSQL extension to partition tables following a foreign key
Name:		%{sname}%{pgmajorversion}
Version:	1.7.0
Release:	1%{?dist}
License:	GPLv2
Source0:	http://api.pgxn.org/dist/%{sname}/%{version}/%{sname}-%{version}.zip
Patch0:		%{sname}-pg%{pgmajorversion}-makefile-pgxs.patch
URL:		http://pgxn.org/dist/pg_fkpart/
BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros
Requires:	postgresql%{pgmajorversion}-server
BuildArch:	noarch

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_min_requires
%endif

%description
pg_fkpart is a PostgreSQL extension to partition tables following a foreign key
of a table.

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
USE_PGXS=1 %make_install install DESTDIR=%{buildroot}
# Install README and howto file under PostgreSQL installation directory:
%{__install} -d %{buildroot}%{pginstdir}/doc/extension
%{__install} -m 644 README.md  %{buildroot}%{pginstdir}/doc/extension/README-%{sname}.md

%files
%doc %{pginstdir}/doc/extension/README-%{sname}.md
%if 0%{?rhel} && 0%{?rhel} <= 6
%doc LICENSE
%else
%license LICENSE
%endif
%{pginstdir}/share/extension/%{sname}.control
%{pginstdir}/share/extension/%{sname}*.sql

%changelog
* Fri Jul 24 2020 Devrim Gündüz <devrim@gunduz.org> - 1.7.0-1
- Update to 1.7.0

* Thu Sep 26 2019 Devrim Gündüz <devrim@gunduz.org> - 1.6.0-1.2
- Rebuild for PostgreSQL 12

* Mon Oct 15 2018 Devrim Gündüz <devrim@gunduz.org> - 1.6.0-1.1
- Rebuild against PostgreSQL 11.0

* Fri Apr 28 2017 - Devrim Gündüz <devrim@gunduz.org> 1.6.0-1
- Update to 1.6.0

* Sat Aug 13 2016 - Devrim Gündüz <devrim@gunduz.org> 1.5.0-1
- Update to 1.5.0

* Thu Mar 3 2016 - Devrim Gündüz <devrim@gunduz.org> 1.3.0-1
- Update to 1.3.0

* Tue Jan 26 2016 - Devrim Gündüz <devrim@gunduz.org> 1.2.2-1
- Update to 1.2.2
- Move docs to new directory
- Update patch0
- Unified spec file for all platforms.

* Mon May 4 2015 - Devrim Gündüz <devrim@gunduz.org> 1.0-1
- Initial packaging

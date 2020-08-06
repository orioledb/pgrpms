%global sname tdigest

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_compiler_at10
%endif

Summary:	t-digest implementation for PostgreSQL
Name:		%{sname}%{pgmajorversion}
Version:	1.0.0
Release:	1%{?dist}
License:	BSD
Source0:	https://github.com/tvondra/%{sname}/archive/v%{version}.tar.gz
Patch0:		%{sname}-pg%{pgmajorversion}-makefile-pgxs.patch
URL:		https://github.com/tvondra/%{sname}
BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros
Requires:	postgresql%{pgmajorversion}-server

%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_min_requires
%endif

%description
This PostgreSQL extension implements t-digest, a data structure for on-line
accumulation of rank-based statistics such as quantiles and trimmed means.
The algorithm is also very friendly to parallel programs.

The accuracy of estimates produced by t-digests can be orders of magnitude
more accurate than those produced by previous digest algorithms in spite of
the fact that t-digests are much more compact when stored on disk.

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
%{__make} USE_PGXS=1 %{?_smp_mflags} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%license LICENSE
%{pginstdir}/lib/%{sname}.so
%{pginstdir}/share/extension/%{sname}*.sql
%{pginstdir}/share/extension/%{sname}.control

%ifarch ppc64 ppc64le
 %else
 %if %{pgmajorversion} >= 11 && %{pgmajorversion} < 90
  %if 0%{?rhel} && 0%{?rhel} <= 6
  %else
   %{pginstdir}/lib/bitcode/%{sname}*.bc
   %{pginstdir}/lib/bitcode/%{sname}/*.bc
  %endif
 %endif
%endif

%changelog
* Thu Aug 6 2020 Devrim Gündüz <devrim@gunduz.org> - 1.0.0-1
- Initial RPM packaging for PostgreSQL RPM Repository
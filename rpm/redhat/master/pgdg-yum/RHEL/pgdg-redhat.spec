Name:		pgdg-redhat-repo
Version:	42.0
Release:	4
Summary:	PostgreSQL PGDG RPMs- Yum Repository Configuration for Red Hat / CentOS / Scientific Linux
License:	PostgreSQL
URL:		https://yum.postgresql.org
Source0:	https://yum.postgresql.org/RPM-GPG-KEY-PGDG
Source2:	pgdg-redhat-all.repo
BuildArch:	noarch
Requires:	/etc/redhat-release
Obsoletes:	pgdg-centos12 pgdg-redhat12 pgdg-sl12
Obsoletes:	pgdg-centos11 pgdg-redhat11 pgdg-sl11
Obsoletes:	pgdg-centos10 pgdg-redhat10 pgdg-sl10
Obsoletes:	pgdg-centos96 pgdg-redhat96 pgdg-sl96
Obsoletes:	pgdg-centos95 pgdg-redhat95 pgdg-sl95
Obsoletes:	pgdg-centos94 pgdg-redhat94 pgdg-sl94

%description
This package contains yum configuration for Red Hat Enterprise Linux, CentOS
 and Scientific Linux. and also the GPG key for PGDG RPMs.

%prep
%setup -q  -c -T

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dpm 644 %{SOURCE0} \
	%{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-PGDG

%{__install} -dm 755 %{buildroot}%{_sysconfdir}/yum.repos.d
%{__install} -pm 644 %{SOURCE2}  \
	%{buildroot}%{_sysconfdir}/yum.repos.d/

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/*
%dir %{_sysconfdir}/pki/rpm-gpg
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Wed Apr 17 2019 Devrim Gündüz <devrim@gunduz.org> - 42.0-4
- Remove major version from GPG file name in the repo file as well.

* Tue Apr 16 2019 Devrim Gündüz <devrim@gunduz.org> - 42.0-3
- Remove major version from GPG file name, per various reports.

* Thu Apr 11 2019 Devrim Gündüz <devrim@gunduz.org> - 42.0-2
- Disable v12 testing repo, it is still in development phase. Per Dave Page.

* Wed Apr 10 2019 Devrim Gündüz <devrim@gunduz.org> - 42.0
- The new repo package, that contains all supported distros.

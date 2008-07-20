Summary:	Enhanced WHOIS client on steroids
Name:		bw-whois
Version:	5.0
Release:	%mkrel 1
License:	GPL or Artistic
Group:          Networking/Other
URL:		http://whois.bw.org
Source0:	whois-%{version}.tar.bz2
Patch0:		whois-config.diff
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
BW Whois is a whois client designed to work with the new "Shared
Registration System" whois introduced 1 December 1999. This new
system has proved to be remarkably disorganized and inconsistent,
resulting in tremendous confusion for those of us who need to
find the ownership of a domain now and then.

%prep

%setup -q -n whois-%{version}
%patch0 -p1

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{perl_vendorlib}
install -d %{buildroot}%{_mandir}/man1

install -m755 whois %{buildroot}%{_bindir}/%{name}
install -m644 whois.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -m644 whois.conf %{buildroot}%{_sysconfdir}/%{name}/
install -m644 tld.conf %{buildroot}%{_sysconfdir}/%{name}/
install -m644 sd.conf %{buildroot}%{_sysconfdir}/%{name}/
install -m644 bwInclude.pm %{buildroot}%{perl_vendorlib}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc DISCLAIMER HISTORY INSTALL README create_whois.sql whois-*.html whois.txt
%config(noreplace) %{_sysconfdir}/%{name}/tld.conf
%config(noreplace) %{_sysconfdir}/%{name}/whois.conf
%config(noreplace) %{_sysconfdir}/%{name}/sd.conf
%{_bindir}/%{name}
%{perl_vendorlib}/bwInclude.pm
%{_mandir}/man1/%{name}.1*

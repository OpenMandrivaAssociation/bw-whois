Summary:	Enhanced WHOIS client on steroids
Name:		bw-whois
Version:	5.0
Release:	%mkrel 2
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


%changelog
* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 5.0-2mdv2010.0
+ Revision: 424700
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 5.0-1mdv2009.0
+ Revision: 238944
- 5.0
- rediffed P0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 3.4-4mdv2007.0
+ Revision: 101624
- Import bw-whois

* Sat Jul 15 2006 Oden Eriksson <oeriksson@mandriva.com> 3.4-4mdv2007.0
- rebuild

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 3.4-3mdk
- rebuild
- fix autodeps

* Mon May 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 3.4-2mdk
- build release


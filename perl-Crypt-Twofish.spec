%define upstream_name    Crypt-Twofish
%define upstream_version 2.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 8

Summary:	Crypt-Twofish module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Twofish is a 128-bit symmetric block cipher with a variable length (128, 192,
or 256-bit) key, developed by Counterpane Labs. It is unpatented and free for
all uses, as described at http://www.counterpane.com/twofish.html.

This module implements Twofish encryption. It supports the Crypt::CBC interface

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*/Crypt/Twofish.pm
%{perl_vendorlib}/*/auto/Crypt/Twofish
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-7mdv2012.0
+ Revision: 765139
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-6
+ Revision: 763653
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-5
+ Revision: 676729
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-4
+ Revision: 676706
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.140.0-3
+ Revision: 676627
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.140.0-2mdv2011.0
+ Revision: 555723
- rebuild

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 2.140.0-1mdv2011.0
+ Revision: 553078
- update to 2.14

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.130.0-1mdv2010.0
+ Revision: 403040
- rebuild using %%perl_convert_version

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 2.13-1mdv2010.0
+ Revision: 376148
- update to new version 2.13

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.12-4mdv2009.0
+ Revision: 256379
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.12-2mdv2008.1
+ Revision: 152045
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.12-1mdv2008.1
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 2.12-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.12-1mdk
- initial Mandriva package


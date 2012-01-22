%define upstream_name    Crypt-Twofish
%define upstream_version 2.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

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

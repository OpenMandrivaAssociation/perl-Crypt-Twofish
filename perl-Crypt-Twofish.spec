%define real_name Crypt-Twofish

Summary:	Crypt-Twofish module for perl 
Name:		perl-%{real_name}
Version:	2.12
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel

%description
Twofish is a 128-bit symmetric block cipher with a variable length (128, 192,
or 256-bit) key, developed by Counterpane Labs. It is unpatented and free for
all uses, as described at http://www.counterpane.com/twofish.html.

This module implements Twofish encryption. It supports the Crypt::CBC interface

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

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



#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Catalyst
%define	pnam	Plugin-Config-YAML
Summary:	Catalyst::Plugin::Config::YAML - Configure your Catalyst application via an YAML file
Summary(pl.UTF-8):	Catalyst::Plugin::Config::YAML - konfiguracja aplikacji Catalysta poprzez plik YAML
Name:		perl-Catalyst-Plugin-Config-YAML
Version:	0.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2eaffe703ec62ccf1429d3ab48a64656
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Config-YAML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst
BuildRequires:	perl-Path-Class
BuildRequires:	perl-YAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Catalyst plugin enables you to configure your Catalyst
application with an external YAML file instead of somewhere in your
application code.

This is useful for example if you want to quickly change the
configuration for different deployment environments (like development,
testing or production) without changing your code.

%description -l pl.UTF-8
Ta wtyczka Catalysta pozwala na konfigurowanie aplikacji Catalysta
przy użyciu zewnętrznego pliku YAML zamiast bezpośrednio w kodzie
aplikacji.

Jest to przydatne na przykład jeśli chcemy szybko zmienić konfigurację
dla różnych środowisk (jak rozwojowe, testowe lub produkcyjne) bez
modyfikowania kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Catalyst/Plugin/Config
%{perl_vendorlib}/Catalyst/Plugin/Config/*.pm
%{_mandir}/man3/*

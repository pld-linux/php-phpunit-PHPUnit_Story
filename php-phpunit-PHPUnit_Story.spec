%define		status		stable
%define		pearname	PHPUnit_Story
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Story extension for PHPUnit to facilitate Behaviour-Driven Development
Name:		php-phpunit-PHPUnit_Story
Version:	1.0.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	0094f35333a8db544a558f016d16b03a
URL:		http://pear.phpunit.de/package/PHPUnit_Story/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-spl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Story extension for PHPUnit to facilitate Behaviour-Driven Development

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/PHPUnit_Story/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PHPUnit/Extensions/Story

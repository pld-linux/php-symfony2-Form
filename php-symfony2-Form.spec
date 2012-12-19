%define		status		stable
%define		pearname	Form
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Form Component
Name:		php-symfony2-Form
Version:	2.1.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	8af4f2e523ff1724a41fdbdb3d14a960
URL:		http://pear.symfony.com/package/Form/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-EventDispatcher
Requires:	php-symfony2-Locale
Requires:	php-symfony2-Validator
Suggests:	php-symfony2-HttpFoundation
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Form Component

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist

# fixups
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/CHANGELOG.md .
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/.gitattributes
rm .%{php_pear_dir}/Symfony/Component/%{pearname}/.gitignore
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Form
%{php_pear_dir}/Symfony/Component/Form/*.php
%{php_pear_dir}/Symfony/Component/Form/Event
%{php_pear_dir}/Symfony/Component/Form/Exception
%{php_pear_dir}/Symfony/Component/Form/Extension
%{php_pear_dir}/Symfony/Component/Form/Guess
%{php_pear_dir}/Symfony/Component/Form/Util

%dir %{php_pear_dir}/Symfony/Component/Form/Resources
%{php_pear_dir}/Symfony/Component/Form/Resources/config

%dir %{php_pear_dir}/Symfony/Component/Form/Resources/translations
%lang(bg) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.bg.xlf
%lang(ca) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.ca.xlf
%lang(cs) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.cs.xlf
%lang(da) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.da.xlf
%lang(de) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.de.xlf
%lang(en) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.en.xlf
%lang(es) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.es.xlf
%lang(et) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.et.xlf
%lang(eu) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.eu.xlf
%lang(fa) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.fa.xlf
%lang(fi) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.fi.xlf
%lang(fr) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.fr.xlf
%lang(he) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.he.xlf
%lang(hr) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.hr.xlf
%lang(hu) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.hu.xlf
%lang(hy) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.hy.xlf
%lang(id) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.id.xlf
%lang(it) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.it.xlf
%lang(ja) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.ja.xlf
%lang(lb) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.lb.xlf
%lang(lt) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.lt.xlf
%lang(mn) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.mn.xlf
%lang(nb) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.nb.xlf
%lang(nl) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.nl.xlf
%lang(pl) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.pl.xlf
%lang(pt) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.pt.xlf
%lang(pt_BR) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.pt_BR.xlf
%lang(ro) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.ro.xlf
%lang(ru) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.ru.xlf
%lang(sk) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.sk.xlf
%lang(sl) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.sl.xlf
# XXX verify
%lang(sr@cyrl) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.sr_Cyrl.xlf
%lang(sr@latin) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.sr_Latn.xlf
%lang(sv) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.sv.xlf
# XXX ru_UA ?
%lang(ua) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.ua.xlf
%lang(zh_CN) %{php_pear_dir}/Symfony/Component/Form/Resources/translations/validators.zh_CN.xlf

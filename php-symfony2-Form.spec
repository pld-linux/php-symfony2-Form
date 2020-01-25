%define		package	Form
%define		php_min_version 5.3.9
Summary:	Symfony2 Form Component
Name:		php-symfony2-Form
Version:	2.7.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	8e01352cf167245276af02ca62f5d5bf
URL:		http://symfony.com/doc/2.7/components/form/index.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(hash)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Requires:	php-symfony2-EventDispatcher >= 2.1
Requires:	php-symfony2-Intl >= 2.4
Requires:	php-symfony2-OptionsResolver >= 2.6
Requires:	php-symfony2-PropertyAccess >= 2.3
Suggests:	php-symfony2-FrameworkBundle
Suggests:	php-symfony2-Security
Suggests:	php-symfony2-TwigBridge
Suggests:	php-symfony2-Validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Form provides tools for defining forms, rendering and mapping request
data to related models. Furthermore it provides integration with the
Validation component.

%prep
%setup -q -n form-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Form
%{php_data_dir}/Symfony/Component/Form/*.php
%{php_data_dir}/Symfony/Component/Form/ChoiceList
%{php_data_dir}/Symfony/Component/Form/Deprecated
%{php_data_dir}/Symfony/Component/Form/Exception
%{php_data_dir}/Symfony/Component/Form/Extension
%{php_data_dir}/Symfony/Component/Form/Guess
%{php_data_dir}/Symfony/Component/Form/Util

%dir %{php_data_dir}/Symfony/Component/Form/Resources
%{php_data_dir}/Symfony/Component/Form/Resources/config

%dir %{php_data_dir}/Symfony/Component/Form/Resources/translations
%lang(ar) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.ar.xlf
%lang(az) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.az.xlf
%lang(bg) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.bg.xlf
%lang(ca) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.ca.xlf
%lang(cs) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.cs.xlf
%lang(da) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.da.xlf
%lang(de) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.de.xlf
%lang(el) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.el.xlf
%lang(en) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.en.xlf
%lang(es) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.es.xlf
%lang(et) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.et.xlf
%lang(eu) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.eu.xlf
%lang(fa) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.fa.xlf
%lang(fi) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.fi.xlf
%lang(fr) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.fr.xlf
%lang(gl) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.gl.xlf
%lang(he) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.he.xlf
%lang(hr) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.hr.xlf
%lang(hu) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.hu.xlf
%lang(hy) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.hy.xlf
%lang(id) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.id.xlf
%lang(it) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.it.xlf
%lang(ja) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.ja.xlf
%lang(lb) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.lb.xlf
%lang(lt) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.lt.xlf
%lang(lv) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.lv.xlf
%lang(mn) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.mn.xlf
%lang(nb) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.nb.xlf
%lang(nl) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.nl.xlf
%lang(pl) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.pl.xlf
%lang(pt) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.pt.xlf
%lang(pt_BR) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.pt_BR.xlf
%lang(ro) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.ro.xlf
%lang(ru) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.ru.xlf
%lang(sk) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.sk.xlf
%lang(sl) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.sl.xlf
%lang(sr@cyrillic) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.sr_Cyrl.xlf
%lang(sr@latin) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.sr_Latn.xlf
%lang(sv) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.sv.xlf
%lang(uk) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.uk.xlf
%lang(zh_CN) %{php_data_dir}/Symfony/Component/Form/Resources/translations/validators.zh_CN.xlf

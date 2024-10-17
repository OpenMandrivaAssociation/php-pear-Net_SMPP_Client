%define		_class		Net
%define		_subclass	SMPP
%define		upstream_name	%{_class}_%{_subclass}_Client

Name:		php-pear-%{upstream_name}
Version:	0.3.2
Release:	9
Summary:	SMPP v3.4 client
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_SMPP_Client/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires: php-pear
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Net_SMPP_Client is a package for communicating with SMPP servers,
built with Net_SMPP. It can be used to send SMS messages, among other
things.

Features:
- PDU stack keeps track of which PDUs have crossed the wire
- Keeps track of the connection state, and won't let you send PDUs if
  the state is incorrect.
- Supports SMPP vendor extensions.

%prep
%setup -qc
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-7mdv2011.0
+ Revision: 679500
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-6mdv2011.0
+ Revision: 613737
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.2-5mdv2010.1
+ Revision: 468719
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.2-4mdv2010.0
+ Revision: 441493
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-3mdv2009.1
+ Revision: 322498
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-2mdv2009.0
+ Revision: 268961
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 06 2008 Funda Wang <fwang@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 216495
- adopt to mandriva style
- import php-pear-Net_SMPP_Client



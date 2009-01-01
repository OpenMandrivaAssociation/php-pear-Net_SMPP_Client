%define		_class		Net
%define		_subclass	SMPP
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}_Client

Summary:	SMPP v3.4 client
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Net_SMPP_Client/
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Net_SMPP_Client is a package for communicating with SMPP servers,
built with Net_SMPP. It can be used to send SMS messages, among other
things.

Features:
- PDU stack keeps track of which PDUs have crossed the wire
- Keeps track of the connection state, and won't let you send PDUs if
  the state is incorrect.
- Supports SMPP vendor extensions.

In PEAR status of this package is: %{_status}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT

install -d %buildroot%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/*.php %buildroot%{_datadir}/pear/%{_class}/%{_subclass}/

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml

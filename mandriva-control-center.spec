Name:           mandriva-control-center
Version:        0.5
Release:        3
Summary:        Mandriva control enter
Group:          Development/Python
License:        GPLv2+
URL:            http://www.mandriva.com
Source0:        %{name}-%{version}.tar.gz
Requires:	qt-components-desktop
BuildArch:	noarch
Requires:	systemd
Requires:	libuser
Requires:	libuser-python
Requires:	python-qt4
Requires:	python-dbus
%py_requires -d

%description
Mandriva control center preview

%prep
%setup -q -n %{name}-%{version}

%build
unset PYTHONDONTWRITEBYTECODE
%{__python} setup.py build

%install
unset PYTHONDONTWRITEBYTECODE
%{__python} setup.py install --install-lib=/usr/share/mandriva  --install-data=/usr/share/mandriva -O1 --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/mcc2-users
%{_bindir}/mcc2-services
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.mcc2.Services.conf
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.mcc2.Sshd.conf
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.mcc2.Users.conf
%{_sysconfdir}/dbus-1/system.d/org.mandrivalinux.mcc2.Grub.conf
%{_datadir}/dbus-1/system-services/org.mandrivalinux.mcc2.Services.service
%{_datadir}/dbus-1/system-services/org.mandrivalinux.mcc2.Sshd.service
%{_datadir}/dbus-1/system-services/org.mandrivalinux.mcc2.Users.service
%{_datadir}/dbus-1/system-services/org.mandrivalinux.mcc2.Grub.service
%{_datadir}/polkit-1/actions/org.mandrivalinux.mcc2.policy
%{_datadir}/polkit-1/actions/org.mandrivalinux.mcc2.services.policy
%{_datadir}/polkit-1/actions/org.mandrivalinux.mcc2.sshd.policy
%{_datadir}/polkit-1/actions/org.mandrivalinux.mcc2.grub.policy
%{_datadir}/polkit-1/actions/org.mandrivalinux.mcc2.users.policy
%{_datadir}/kde4/services/settings-mandriva.desktop
%{_datadir}/apps/mandriva-control-center/*
%{_datadir}/applications/kde4/mcc2-services.desktop
%{_datadir}/applications/kde4/mcc2-users.desktop
%{_datadir}/mandriva/*


%changelog
* Wed Aug 03 2011 Wiliam Alves de Souza <wiliam@mandriva.com> 0.5-1
+ Revision: 693074
- new release 0.5

* Mon Jul 04 2011 Wiliam Alves de Souza <wiliam@mandriva.com> 0.4-1
+ Revision: 688678
- new release 0.4

* Tue Jun 21 2011 Wiliam Alves de Souza <wiliam@mandriva.com> 0.3-1
+ Revision: 686518
- new release 0.3

* Tue Jun 07 2011 Wiliam Alves de Souza <wiliam@mandriva.com> 0.2-1
+ Revision: 683086
- new release 0.2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file

* Mon May 16 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.1-2
+ Revision: 675122
- Missing requires

* Mon May 16 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.1-1
+ Revision: 675117
- Added initial preview version to cooker
- Renamed to correct package name
- Created package structure for mcc2.


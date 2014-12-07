Summary:        Mandriva control enter
Name:           mandriva-control-center
Version:        0.5
Release:        11
Group:          Development/Python
License:        GPLv2+
Url:            http://www.mandriva.com
Source0:        %{name}-%{version}.tar.gz
BuildArch:	noarch
%py_requires -d
Requires:	libuser
Requires:	libuser-python
Requires:	python-qt4
Requires:	python-dbus
Requires:	qt-components-desktop
Requires:	systemd

%description
Mandriva control center preview

%prep
%setup -q

%build
unset PYTHONDONTWRITEBYTECODE
%{__python} setup.py build

%install
unset PYTHONDONTWRITEBYTECODE
%{__python} setup.py install \
	--install-lib=/usr/share/mandriva \
	--install-data=/usr/share/mandriva \
	-O1 --skip-build --root %{buildroot}

%files
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


%define libname %mklibname KF6Sonnet
%define devname %mklibname KF6Sonnet -d
%define git 20231013

Name: kf6-sonnet
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/sonnet/-/archive/master/sonnet-master.tar.bz2#/sonnet-%{git}.tar.bz2
Summary: Spelling framework for Qt
URL: https://invent.kde.org/frameworks/sonnet
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(libvoikko)
BuildRequires: aspell aspell-devel
BuildRequires: hspell-devel
BuildRequires: pkgconfig(zlib)
Requires: %{libname} = %{EVRD}

%description
Spelling framework for Qt

%package -n %{libname}
Summary: Spelling framework for Qt
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Spelling framework for Qt

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Spelling framework for Qt

%prep
%autosetup -p1 -n sonnet-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/sonnet.*
%{_bindir}/parsetrigrams6

%files -n %{devname}
%{_includedir}/KF6/Sonnet
%{_includedir}/KF6/SonnetCore
%{_includedir}/KF6/SonnetUi
%{_libdir}/cmake/KF6Sonnet
%{_qtdir}/doc/KF6SonnetCore.*
%{_qtdir}/doc/KF6SonnetUi.*

%files -n %{libname}
%{_libdir}/libKF6SonnetCore.so*
%{_libdir}/libKF6SonnetUi.so*
%{_qtdir}/qml/org/kde/sonnet
# FIXME potentially split the backends into separate packages,
# esp. voikko (Finnish only) and hspell (Hebrew only) aren't useful
# to everyone
%dir %{_qtdir}/plugins/kf6/sonnet
%{_qtdir}/plugins/kf6/sonnet/sonnet_aspell.so
%{_qtdir}/plugins/kf6/sonnet/sonnet_hspell.so
%{_qtdir}/plugins/kf6/sonnet/sonnet_hunspell.so
%{_qtdir}/plugins/kf6/sonnet/sonnet_voikko.so

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/sonnet6widgets.so

Name:       com.flap.bird
Summary:    dFlap
Version:    1.0.0
Release:    1
Group:      Qt/Qt
License:    BSD-3-Clause
URL:        https://sorydima.github.io/dFlap
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(aurorawebview)
BuildRequires:  pkgconfig(auroraapp)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Network)

%description
In Flappy Rocket, you control a futuristic space rocket navigating through an endless field of space debris and alien towers. Test your reflexes and precision as you fly through narrow gaps between obstacles. The goal is simple: keep flying as long as you can without crashing! Collect power-ups along the way to boost your score and unlock new rock!

%prep
%autosetup

%build
%qmake5
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%defattr(644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/*

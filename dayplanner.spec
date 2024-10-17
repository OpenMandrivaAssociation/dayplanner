%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(DP::CoreModules\\)'
%else
%define _requires_exceptions perl\(DP::CoreModules\)
%endif

Summary:	An easy and clean Day Planner
Name:		dayplanner
Version:	0.11
Release:	2
Group:		Office
License:	GPLv3+
URL:		https://www.day-planner.org/
Source0:	http://download.gna.org/dayplanner/%{name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Locale::gettext)
BuildArch:	noarch

%description
Day Planner is a simple time management program.

Day Planner is designed to help you easily manage your time.
It can manage appointments, birthdays and more. It makes sure you
remember your appointments by popping up a dialog box reminding you about it.

%files -f dayplanner.lang
# Note to packagers: Please leave COPYING in here as this package is distributed
#  from the software website aswell
%doc AUTHORS COPYING NEWS THANKS TODO ./doc/*
%{_bindir}/dayplanner
%{_bindir}/dayplanner-daemon
%{_bindir}/dayplanner-notifier
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_iconsdir}/dayplanner*.png
%{_miconsdir}/dayplanner*.png
%{_liconsdir}/dayplanner*.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
# Nothing

%install
%makeinstall_std prefix=/usr

# Install the icons
install -m644 ./art/dayplanner-24x24.png -D %{buildroot}%{_iconsdir}/dayplanner.png
install -m644 ./art/dayplanner-16x16.png -D %{buildroot}%{_miconsdir}/dayplanner.png
install -m644 ./art/dayplanner-48x48.png -D %{buildroot}%{_liconsdir}/dayplanner.png
# (High contrast icons)
install -m644 ./art/dayplanner_HC24.png -D %{buildroot}%{_iconsdir}/dayplanner_HC.png
install -m644 ./art/dayplanner_HC16.png -D %{buildroot}%{_miconsdir}/dayplanner_HC.png
install -m644 ./art/dayplanner_HC48.png -D %{buildroot}%{_liconsdir}/dayplanner_HC.png

# Find the localization
%find_lang %{name}


Name: 		Watcher
Version: 	0.3
Release:        1%{?dist}
Summary: 	Inotify watcher

License: 	MIT
Group:		System Environment/Base
URL:	 	https://github.com/guard43ru/Watcher
Source0: 	%{url}/archive/%{version}.tar.gz

Requires:	python-inotify
Requires:	python-daemon
Requires:	python-lockfile
Requires:	python-chardet

BuildRequires:	systemd-units
BuildArch:	noarch

%description
Watcher is a daemon that watches specified files/folders for changes and
fires commands in response to those changes. It is similar to incron,
however, configuration uses a simpler to read ini file instead of a plain
text file. Unlike incron it can also recursively monitor directories.


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
%{make_install}


%files
%{_bindir}/watcher
%{_sysconfdir}/watcher.conf
%{_unitdir}/watcher.service

%changelog
* Wed Apr  6 2016 Roman Ginovich
- Initial version of the package

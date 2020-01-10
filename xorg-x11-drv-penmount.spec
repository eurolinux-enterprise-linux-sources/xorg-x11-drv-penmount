%global tarball xf86-input-penmount
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

Summary:   Xorg X11 penmount input driver
Name:      xorg-x11-drv-penmount
Version:   1.5.0
Release:   2%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Patch01:   0001-Don-t-free-anything-in-PreInit-let-the-server-call-U.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.10.0-1
BuildRequires: xorg-x11-proto-devel >= 7.2-10

Requires:  Xorg %(xserver-sdk-abi-requires ansic)
Requires:  Xorg %(xserver-sdk-abi-requires xinput)

%description 
X.Org X11 penmount input driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch01 -p1

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/penmount_drv.so
%{_mandir}/man4/penmount.4*

%changelog
* Tue Jul 19 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-2
- Stop crashes on failed PreInit

* Tue Jun 28 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.5.0-1
- penmount 1.5.0 (#713812)

* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-5
- Use global instead of define as per Packaging Guidelines.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.4.0-4.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 17 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.4.0-3
- penmount-1.4.0-abi.patch: Cope with XINPUT ABI 7.

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.4.0-2.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.4.0-1
- penmount 1.4.0

* Thu Mar 20 2008 Adam Jackson <ajax@redhat.com> 1.3.0-1
- penmount 1.3.0

* Thu Feb 21 2008 Adam Jackson <ajax@redhat.com> 1.2.1-1
- penmount 1.2.1

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.0-7
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.1.0-6
- Rebuild for build id

* Thu Jul 12 2007 Adam Jackson <ajax@redhat.com> 1.1.0-5
- Fix build with new inputproto.

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.1.0-4
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.1.0-3
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Sat Jun 17 2006 Mike A. Harris <mharris@redhat.com> 1.1.0-2
- Actually build 1.1.0 for FC6.
- Remove mandir ownership from package.

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 1.1.0-1
- Update to 1.1.0 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 1.0.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 1.0.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.0.5-1
- Updated xorg-x11-drv-penmount to version 1.0.0.5 from X11R7.0
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.4-1
- Updated xorg-x11-drv-penmount to version 1.0.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-penmount to version 1.0.0.2 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-penmount to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for penmount input driver generated automatically
  by my xorg-driverspecgen script.

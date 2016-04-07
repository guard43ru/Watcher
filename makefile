.PHONY: install uninstall

install:

	mkdir -p $(DESTDIR)/usr/bin
	mkdir -p $(DESTDIR)/etc	
	mkdir -p $(DESTDIR)/usr/lib/systemd/system/
	mkdir -p $(DESTDIR)/var/lib/watcher
	cp watcher.py $(DESTDIR)/usr/bin/watcher
	cp watcher.conf $(DESTDIR)/etc/
	cp ./package/init/watcher.systemd $(DESTDIR)/usr/lib/systemd/system/watcher.service

uninstall:

	rm -f $(DESTDIR)/usr/bin/watcher
	rm -f $(DESTDIR)/etc/watcher.conf
	rm -f $(DESTDIR)/usr/lib/systemd/system/watcher.service
	rm -rf $(DESTDIR)/var/lib/watcher
